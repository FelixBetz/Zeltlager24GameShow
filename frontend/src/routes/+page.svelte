<script lang="ts">
	import CreateTeams from '$lib/CreateTeams/CreateTeams.svelte';
	import ListGame from '$lib/Games/ListGame/ListGame.svelte';
	import Score from '$lib/Score/Score.svelte';
	import { apiGetGame } from '$lib/api/apiGame';
	import { GameState, type Game, getDefaultGame } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';

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

<div class="container">
	<!--
	<div class="row">
		<OverallScore teams={game.teams} />
	</div>
	-->

	<div>
		{#if game.state == GameState.IDLE}
			IDLE
		{:else if game.state === GameState.CREATING_TEAMS}
			<CreateTeams {game} />
		{:else if game.state === GameState.GAME_1}
			<ListGame {game} />
		{:else if game.state == GameState.GAME_2}
			IDLE
		{:else if game.state == GameState.GAME_3}
			IDLE
		{:else if game.state == GameState.GAME_4}
			IDLE
		{:else if game.state == GameState.GAME_5}
			IDLE
		{:else if game.state == GameState.SCORE}
			<Score teams={game.teams} />
		{/if}
	</div>
</div>
