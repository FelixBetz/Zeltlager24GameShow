<script lang="ts">
	import ListGameAdmin from '../../lib/Games/ListGame/ListGameAdmin.svelte';

	import CreateTeamsAdmin from '$lib/CreateTeams/CreateTeamsAdmin.svelte';

	import { apiGetGame } from '$lib/api/apiGame';
	import { GameState, type Game, getDefaultGame } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';

	import SwitchTeam from '$lib/Admin/SwitchActiveTeam.svelte';
	import SwitchGameState from '$lib/Admin/SwitchGameState.svelte';
	import TeamOverview from '$lib/Admin/TeamOverview.svelte';

	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let game: Game = getDefaultGame();
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

<div class="row">
	<div class="col-2">
		<SwitchGameState {game} />
	</div>
	<div class="col-3">
		<TeamOverview {game} />
		<hr />
		<SwitchTeam {game} />
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
		{:else if game.state == GameState.SCORE}
			IDLE
		{/if}
	</div>
</div>

<style>
</style>
