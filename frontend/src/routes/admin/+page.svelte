<script lang="ts">
	import ListGameAdmin from '../../lib/Games/ListGame/ListGameAdmin.svelte';
	import AvatarImage from '$lib/AvatarImage.svelte';
	import CreateTeamsAdmin from '$lib/CreateTeams/CreateTeamsAdmin.svelte';

	import { apiAdminSwitchState } from '$lib/api/apiAdmin';
	import { apiGetGame } from '$lib/api/apiGame';
	import { GameState, type Game } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';

	const states: string[] = Object.values(GameState);

	function onClickSwitchState(pState: string) {
		apiAdminSwitchState(pState);
	}

	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let game: Game = {
		teams: [],
		state: GameState.IDLE
	};
	let isRequestOngoing = false;
	async function cyclicInterval() {
		if (!isRequestOngoing) {
			isRequestOngoing = true;
			game = await apiGetGame();
			isRequestOngoing = false;
		}
	}

	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 1000);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<div>
	asfd
	<i class="bi bi-plus-circle" />
</div>
<div class="row">
	<div class="col-2">
		<h1>Game States</h1>
		<div class="d-grid gap-2">
			{#each states as state}
				<button class="btn btn-primary" on:click={() => onClickSwitchState(state)}>
					{state}
				</button>
			{/each}
		</div>
	</div>
	<div class="col-3">
		<h1>Teams</h1>
		<div class="row">
			<div class="col-12">
				{#each game.teams as team}
					<div class="card">
						<div class="d-flex">
							<div><AvatarImage avatar={team.avatar_url} /></div>
							<div><button><i class="bi bi-plus-circle" /></button></div>
							<div>{team.total_score}</div>
							<div><button><i class="bi bi-minus-circle" /></button></div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
	<div class="col-7">
		<h1>Game</h1>

		{#if game.state == GameState.IDLE}
			IDLE
		{:else if game.state === GameState.CREATING_TEAMS}
			<CreateTeamsAdmin />
		{:else if game.state === GameState.GAME_1}
			<ListGameAdmin />
		{:else if game.state == GameState.GAME_2}
			IDLE
		{:else if game.state == GameState.GAME_3}
			IDLE
		{:else if game.state == GameState.GAME_4}
			IDLE
		{:else if game.state == GameState.GAME_5}
			IDLE
		{:else if game.state == GameState.RESULTS}
			IDLE
		{/if}
	</div>
</div>
