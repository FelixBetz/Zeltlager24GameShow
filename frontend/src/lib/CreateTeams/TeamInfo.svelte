<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import type { Team } from '$lib/types';

	export let team: Team;
	export let size = 100;
</script>

<div class="col text-center">
	<div>
		<AvatarImage {size} avatar={team.avatar_url} />
	</div>

	<div class="team-name">Team {team.name}</div>
</div>

<style>
	.team-name {
		font-size: 1.5rem;
		font-weight: bolder;
	}
</style>
