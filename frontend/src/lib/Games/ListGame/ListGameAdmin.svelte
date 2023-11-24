<script lang="ts">
	import {
		apiListGameGetData,
		apiListGamePlaceItem,
		getDefaultListGameDate,
		ListGameState,
		type ListGameData,
		apiListGameSwitchState,
		apiListGameShowValues
	} from '$lib/api/apiGameListGame';
	import { onDestroy, onMount } from 'svelte';
	import ListGameItems from './ListGameItems.svelte';

	let gameData: ListGameData = getDefaultListGameDate();
	let intervalGameState: string | number | NodeJS.Timeout | undefined;

	let isRequestOngoing = false;
	let inidces: number[] = [];

	let selectedItemIndex = -1;
	let selectedItemPos = -1;

	const states: string[] = Object.values(ListGameState);

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
			gameData = await apiListGameGetData();
			isRequestOngoing = false;
		}
	}

	async function onPlaceClick() {
		await apiListGamePlaceItem(selectedItemIndex, selectedItemPos);

		selectedItemIndex = -1;
		selectedItemPos = -1;
	}

	function onClickSwitchState(pState: string) {
		if (Object.values(ListGameState).includes(pState as ListGameState)) {
			gameData.state = ListGameState[pState as keyof typeof ListGameState];
		}
		apiListGameSwitchState(pState);
	}

	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 100);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<h3>Switch ListGame State</h3>
<div class="row align-items-center">
	{#each states as state}
		<div class="col-2">
			<button
				class="btn btn-primary w-100 {state == gameData.state
					? 'border border-5 border-secondary'
					: ''}"
				on:click={() => onClickSwitchState(state)}
			>
				{state}
			</button>
		</div>
	{/each}
	<div class="col-2">
		<button class="btn btn-info w-100" on:click={() => apiListGameShowValues(true)}>
			Show Values
		</button>
	</div>
	<div class="col-2">
		<button class="btn btn-info w-100" on:click={() => apiListGameShowValues(false)}>
			Hide Values
		</button>
	</div>
</div>
<hr />

{#if gameData.state == ListGameState.IDLE}
	Idle
{:else if gameData.state == ListGameState.WAIT_DRAW}
	dasdf
{:else if gameData.state == ListGameState.PLAY}
	<h3>Play</h3>
	<div class="row">
		<div>
			<div class="row">
				<div class="col">
					<select
						class="form-select"
						aria-label="Default select example"
						bind:value={selectedItemIndex}
					>
						{#each gameData.itemsSorted as item}
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
{/if}
