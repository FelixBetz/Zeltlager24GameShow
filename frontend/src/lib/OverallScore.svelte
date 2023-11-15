<script lang="ts">
	import AvatarImage from './AvatarImage.svelte';
	import type { Team } from './types';

	export let teams: Team[] = [];
</script>

<div class="row">
	{#each teams as team}
		<div class="col">
			<AvatarImage avatar={team.avatar_url} />
			{team.name}
		</div>
	{/each}
</div>
