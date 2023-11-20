<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiAddTeam, apiUpdateCurrentTeam } from '$lib/api/apiAdmin';
	import { apiGetAvatars, apiGetCurrentTeam } from '$lib/api/apiGame';

	import type { CurrentTeam, Team } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
	import TeamInfo from './TeamInfo.svelte';

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

	let avatars: string[] = [];
	let selectedAvatarIdx = -1;
	let team: Team = {
		shortcut: '',
		name: '',
		scores: [],
		total_score: 0,
		avatar_url: '',
		game_life: 0
	};

	function createNewTeam() {
		team.avatar_url = '';
		team.name = '';
		team.shortcut = '';
		team.total_score = 0;
		team.scores = [];
		selectedAvatarIdx = -1;
	}

	function updateUrl(pIdx: number) {
		if (pIdx >= 0 && pIdx < avatars.length) {
			team.avatar_url = avatars[pIdx];
		}
	}
	function onTeamChange(pTeam: Team) {
		apiUpdateCurrentTeam(pTeam);
	}

	$: updateUrl(selectedAvatarIdx);
	$: onTeamChange(team);
	async function cyclicInterval() {
		currentTeam = await apiGetCurrentTeam();
	}
	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	onMount(async () => {
		createNewTeam();

		avatars = [''].concat(await apiGetAvatars());
		intervalGameState = setInterval(cyclicInterval, 100);
	});
	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<div class="row">
	<div class="col-6">
		<form class="row g-3 needs-validation" novalidate>
			<div class="col-md-6">
				<label for="name" class="form-label">Teamname</label>
				<input
					type="text"
					class="form-control"
					id="name"
					placeholder="Teamname"
					bind:value={team.name}
				/>
			</div>
			<div class="col-md-6">
				<label for="shortcut" class="form-label">Kürzel</label>
				<input
					type="text"
					class="form-control"
					id="shortcut"
					placeholder="Kürzel"
					bind:value={team.shortcut}
				/>
			</div>

			<div>
				<div class="avatar-row">
					{#each avatars as avatar, idx}
						<button on:click={() => (selectedAvatarIdx = idx)} class="p-0 m-0">
							<AvatarImage size={50} {avatar} isSelected={idx == selectedAvatarIdx} />
						</button>
					{/each}
				</div>
			</div>

			<div class="col-12">
				<button class="btn btn-primary" type="submit" on:click={() => apiAddTeam(team)}>
					Create Team
				</button>
			</div>
		</form>
	</div>

	<div class="col-6">
		{#if currentTeam.isShow}
			<div>
				<TeamInfo team={currentTeam.team} size={250} />
			</div>
		{/if}
	</div>
</div>

<style>
	.avatar-row {
		display: flex;
		flex-wrap: wrap;
		column-gap: 10px;
		row-gap: 10px;
	}
	.avatar-row button {
		background-color: transparent;
		border: 0px;
	}
</style>
