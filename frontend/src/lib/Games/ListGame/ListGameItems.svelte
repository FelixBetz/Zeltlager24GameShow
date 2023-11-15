<script lang="ts">
	import type { ListGameItem } from '$lib/api/apiGameListGame';
	export let showDetails = false;
	export let items: ListGameItem[];
</script>

<div class="row g-3">
	{#each items as item}
		<div class="col-4">
			<div
				class="item rounded-3 p-2 text-center {item.isPlaced ? 'bg-body-tertiary' : 'bg-primary'}"
			>
				<div class:is-placed={item.isPlaced}>
					{item.label}
					{#if showDetails}
						( {item.index},
						{item.value})
					{/if}
				</div>
			</div>
		</div>
	{/each}
</div>

<style>
	.is-placed {
		opacity: 0.1;
	}
</style>
