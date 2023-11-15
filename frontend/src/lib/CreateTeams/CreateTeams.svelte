<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiGetCurrentTeam } from '$lib/api/apiGame';
	import type { Game, Team } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';

	export let game: Game;

	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let currentTeam: Team = {
		avatar_url: '',
		name: '',
		shortcut: '',
		scores: [],
		total_score: 0,
		game_life: 0
	};

	async function cyclicInterval() {
		currentTeam = await apiGetCurrentTeam();
	}

	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 100);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});
</script>

<h1>Create Team</h1>
<div class="row">
	<div class="col-6">
		<h2>Teams</h2>
		{#each game.teams as team}
			<div>{team.name}</div>
		{/each}
	</div>
	<div class="col-6">
		<h2>Neues Team</h2>
		<div>
			<AvatarImage size={200} avatar={currentTeam.avatar_url} />
		</div>
		<div>
			<div>Name:{currentTeam.name}</div>
			<div>Kürzel:{currentTeam.shortcut}</div>
		</div>
		<pre>
            {JSON.stringify(currentTeam, null, 2)}
        </pre>
	</div>
</div>
