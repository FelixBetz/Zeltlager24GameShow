<script lang="ts">
	import { apiAdminSwitchState } from '$lib/api/apiAdmin';
	import { GameState, type Game } from '$lib/types';

	export let game: Game;
	const states: string[] = Object.values(GameState);

	function onClickSwitchState(pState: string) {
		if (Object.values(GameState).includes(pState as GameState)) {
			game.state = GameState[pState as keyof typeof GameState];
		}
		apiAdminSwitchState(pState);
	}
</script>

<h1>Game States</h1>
<div class="d-grid gap-2">
	{#each states as state}
		<button
			class="btn btn-primary {state == game.state ? 'border border-5 border-secondary' : ''}"
			on:click={() => onClickSwitchState(state)}
		>
			{state}
		</button>
	{/each}
</div>
