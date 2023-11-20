<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiGetAvatars, apiGetCurrentTeam } from '$lib/api/apiGame';
	import type { CurrentTeam, Game } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
	import TeamInfo from './TeamInfo.svelte';

	export let game: Game;
	let avatars: string[] = [];

	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let currentTeam: CurrentTeam = {
		team: {
			avatar_url: '',
			name: '',
			shortcut: '',
			scores: [],
			total_score: 0,
			game_life: 0
		},
		isShow: false
	};

	async function cyclicInterval() {
		currentTeam = await apiGetCurrentTeam();
	}

	onMount(async () => {
		intervalGameState = setInterval(cyclicInterval, 100);
		avatars = await apiGetAvatars();
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<div class="mb-3">
	<h1>Teams</h1>
</div>
<div class="team-row">
	{#each game.teams as team}
		<div>
			<TeamInfo {team} size={250} />
		</div>
	{/each}
</div>
<div class="mt-3">
	<h2>Neues Team</h2>
</div>
<div class="d-flex">
	<div class="me-5">
		{#if currentTeam.isShow}
			<div>
				<TeamInfo team={currentTeam.team} size={250} />
			</div>
		{/if}
	</div>
	<div class="">
		<div class="avatar-row">
			{#each avatars as avatar}
				<div>
					<AvatarImage size={100} {avatar} isSelected={avatar == currentTeam.team.avatar_url} />
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.team-row {
		display: flex;
		flex-wrap: wrap;
		column-gap: 10px;
		row-gap: 10px;
	}
	.avatar-row {
		display: flex;
		flex-wrap: wrap;
		column-gap: 10px;
		row-gap: 10px;
	}
</style>
