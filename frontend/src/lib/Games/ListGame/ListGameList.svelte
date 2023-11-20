<script lang="ts">
	import type { ListGameItem } from '$lib/api/apiGameListGame';

	export let items: ListGameItem[];
	export let minValue: string;
	export let maxValue: string;

	let markerIndices: number[] = [];
	let firstIndex = -1;

	$: createIndices(items);
	function createIndices(pItems: ListGameItem[]) {
		markerIndices = [];
		let isFirst = false;
		let cnt = 2;
		pItems.forEach((item, idx) => {
			if (item.isPlaced && !isFirst) {
				firstIndex = idx;
				isFirst = true;
			}
			markerIndices.push(item.isPlaced ? cnt++ : -1);
		});
	}
</script>

<div class="row justify-content-center g-0 text-center">
	{#if items.length > 0}
		<div class="col-12 mb-4">
			<div class="badge bg-danger fade-in">{minValue}</div>
		</div>

		{#each items as item, idx}
			{#if item.isPlaced}
				<div class="col-12 position-relative p-1">
					{#if idx == firstIndex}
						<span class="position-absolute top-0 start-0 translate-middle index bg-danger fade-in">
							{1}
						</span>
					{/if}
					<div style="margin-left:  20px;">
						<div class:start-item={item.isStartItem} class="fly-in rounded-3 p-2 bg-info">
							{item.label}
							{#if item.isStartItem} ({item.value}){/if}
						</div>
					</div>

					<span class="position-absolute top-100 start-0 translate-middle index bg-danger fade-in">
						{markerIndices[idx]}
					</span>
				</div>
			{/if}
		{/each}

		<div class="col-12 mt-4">
			<div class="badge bg-danger fade-in">{maxValue}</div>
		</div>
	{/if}
</div>

<style>
	.start-item {
		font-weight: bolder;
	}

	.index {
		display: inline-block;
		padding: 4px 15px;
		margin: 0px;
		left: -50px;
		border-radius: 50px; /* Adjust the value to control the roundness */
		background-color: #3498db; /* Set your desired background color */
		color: #fff; /* Set your desired text color */
		position: relative;
		font-size: large;
	}

	.index::before {
		content: '';
		position: absolute;
		top: 50%;
		left: 100%;
		margin-top: -10px; /* Half of the height to center the arrow vertically */
		margin-left: -4px;
		border-width: 10px;
		border-style: solid;
		border-color: transparent transparent transparent var(--bs-danger); /* Set arrow color */
	}

	@keyframes flyIn {
		0% {
			transform: translateX(-100%);
		}
		90% {
			transform: translateX(20%);
		}
		100% {
			transform: translateX(0%);
		}
	}

	@keyframes fadeIn {
		0% {
			opacity: 0;
		}
		50% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}

	.fly-in {
		animation: flyIn 1s ease-out; /* Adjust the duration and easing as needed */
	}
	.fade-in {
		animation: fadeIn 2s ease-out; /* Adjust the duration and easing as needed */
	}

	.badge {
		font-size: large;
	}
</style>
