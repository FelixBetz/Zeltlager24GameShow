<script lang="ts">
	import { API_URL } from '$lib/api/apiUrl';
	export let avatar = '';
	export let size = 50;
	export let isSelected = false;
</script>

<div
	style="width: {size}px; height: {size}px; background-color: var(--bs-gray-600) "
	class="avatar rounded mx-auto d-block border border-5 {isSelected
		? 'border-info'
		: 'border-normal'}"
>
	{#if avatar != ''}
		<img src={API_URL + 'assets/' + avatar} alt={avatar} />
	{/if}
</div>

<style>
	.avatar {
		padding: 3px;
	}
	img {
		width: 100%;
		height: 100%;
	}

	.border-normal {
		border-color: var(--bs-gray-600) !important;
	}
</style>
