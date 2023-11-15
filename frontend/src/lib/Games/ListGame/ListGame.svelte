<script lang="ts">
	import {
		apiGetListGameData,
		getDefaultListGameDate,
		type ListGameData
	} from '$lib/api/apiGameListGame';
	import type { Game } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
	import ListGameList from './ListGameList.svelte';
	import ListGameItems from './ListGameItems.svelte';

	export let game: Game;

	let gameData: ListGameData = getDefaultListGameDate();
	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let isRequestOngoing = false;

	async function cyclicInterval() {
		if (!isRequestOngoing) {
			isRequestOngoing = true;
			gameData = await apiGetListGameData();
			isRequestOngoing = false;
		}
	}
	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 500);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<h1>Test</h1>

<div class="row">
	<div class="col-5 justify-content-center">
		<ListGameList
			items={gameData.placedItems}
			minValue={gameData.minValue}
			maxValue={gameData.maxValue}
		/>
	</div>
	<div class="col-7 unsorted">
		<ListGameItems items={gameData.itemsRandom} />
	</div>
</div>

<style>
</style>
