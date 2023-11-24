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

<div class="row text-center mt-3">
	<div class="d-flex flex-wrap justify-content-center">
		{#each game.teams as team}
			<div class="p-3">
				<TeamInfo {team} size={250} />
			</div>
		{/each}
	</div>
	{#if currentTeam.isShow}
		<div class=" mt-5 mb-5">
			<div class="text-start fs-1 p-0">Neues Team:</div>
			<div class="border border-5 border-light p-0" style="border-style: dashed !important;">
				<div class="row m-3">
					<div class="col" style=" max-width: 300px;">
						<div class="p-2">
							<TeamInfo team={currentTeam.team} size={220} />
						</div>
					</div>

					<div class="col">
						<div class="d-flex justify-content-around flex-wrap p-0 m-0">
							{#each avatars as avatar}
								<div class="p-2 m-0">
									<AvatarImage
										size={100}
										{avatar}
										isSelected={avatar == currentTeam.team.avatar_url}
									/>
								</div>
							{/each}
						</div>
					</div>
				</div>
			</div>
		</div>
	{/if}
</div>
