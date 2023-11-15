<script lang="ts">
	import {
		apiGetListGameData,
		apiPlaceItem,
		getDefaultListGameDate,
		type ListGameData
	} from '$lib/api/apiGameListGame';
	import { onDestroy, onMount } from 'svelte';
	import ListGameItems from './ListGameItems.svelte';

	let gameData: ListGameData = getDefaultListGameDate();
	let intervalGameState: string | number | NodeJS.Timeout | undefined;

	let isRequestOngoing = false;
	let inidces: number[] = [];

	let selectedItemIndex = -1;
	let selectedItemPos = -1;

	let isPlaceValid = false;
	$: isPlaceValid = checkIsPlaceValid(selectedItemIndex, selectedItemPos);
	function checkIsPlaceValid(pSelectedItemIndex: number, pSelectedItemPos: number) {
		let isIndexOk = gameData.itemsRandom.some((item) => item.index === pSelectedItemIndex);
		let isPositionOk = inidces.includes(pSelectedItemPos);

		return isIndexOk && isPositionOk;
	}

	function createIndices(pGameData: ListGameData) {
		inidces = [];
		for (let i = 0; i < pGameData.placedItems.length + 1; i++) {
			inidces.push(i + 1);
		}
		inidces = inidces;
	}
	$: createIndices(gameData);

	async function cyclicInterval() {
		if (!isRequestOngoing) {
			isRequestOngoing = true;
			gameData = await apiGetListGameData();
			isRequestOngoing = false;
		}
	}

	async function onPlaceClick() {
		await apiPlaceItem(selectedItemIndex, selectedItemPos);

		selectedItemIndex = -1;
		selectedItemPos = -1;
	}

	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 500);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<div class="row">
	<div>
		<div class="row">
			<div class="col">
				<select
					class="form-select"
					aria-label="Default select example"
					bind:value={selectedItemIndex}
				>
					{#each gameData.itemsRandom as item}
						{#if !item.isPlaced}
							<option value={item.index}>{item.label}</option>
						{/if}
					{/each}
				</select>
			</div>
			<div class="col">
				<select
					class="form-select"
					aria-label="Default select example"
					bind:value={selectedItemPos}
				>
					{#each inidces as idx}
						<option>{idx}</option>
					{/each}
				</select>
			</div>
			<div class="col" style="background-color: var(light);">
				<button class="btn btn-primary w-100" on:click={onPlaceClick} disabled={!isPlaceValid}>
					Place
				</button>
			</div>
		</div>
	</div>
</div>
<div class="mt-5">
	<ListGameItems items={gameData.itemsSorted} showDetails={true} />
</div>
