<script lang="ts">
	import {
		apiListGameGetData,
		getDefaultListGameDate,
		ListGameState,
		type ListGameData
	} from '$lib/api/apiGameListGame';
	import type { Game } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
	import ListGameList from './ListGameList.svelte';
	import ListGameItems from './ListGameItems.svelte';
	import AvatarImage from '$lib/AvatarImage.svelte';

	export let game: Game;

	const GAME_NAME = 'Spiel1: Füge in Liste ein';

	let gameData: ListGameData = getDefaultListGameDate();
	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let isRequestOngoing = false;

	async function cyclicInterval() {
		if (!isRequestOngoing) {
			isRequestOngoing = true;
			gameData = await apiListGameGetData();
			isRequestOngoing = false;
		}
	}
	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 100);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<h1>{GAME_NAME}</h1>
{#if gameData.state == ListGameState.IDLE}
	<div>IDle</div>
{:else if gameData.state == ListGameState.WAIT_DRAW}
	<div class="row text-center">
		{#each game.teams as team, idx}
			<div class="col">
				<h2>
					{team.name}
				</h2>
				<AvatarImage avatar={team.avatar_url} size={200} isSelected={game.currentTurnTeam == idx} />
			</div>
		{/each}
	</div>
{:else if gameData.state == ListGameState.PLAY}
	<div class="row">
		<div class="col-5 justify-content-center">
			<ListGameList
				items={gameData.itemsSorted}
				minValue={gameData.minValue}
				maxValue={gameData.maxValue}
			/>
		</div>
		<div class="col-7 unsorted">
			<ListGameItems items={gameData.itemsRandom} />
		</div>
	</div>
{:else if gameData.state == ListGameState.SHOW_POINTS}
	Points
{/if}

<style>
</style>
