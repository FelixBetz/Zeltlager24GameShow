<script lang="ts">
	import { apiListGameSwitchCurrentTeam } from '$lib/api/apiGameListGame';
	import type { Game } from '$lib/types';

	export let game: Game;

	function onClickCurrentTeamSwitch(pNum: number) {
		game.currentTurnTeam = pNum;

		apiListGameSwitchCurrentTeam(pNum);
	}
</script>

<h3>Switch Acitve Team</h3>
<div class="d-grid gap-2 align-items-center">
	{#each game.teams as team, idx}
		<div class="">
			<button
				class="btn btn-primary w-100 {idx == game.currentTurnTeam
					? 'border border-4 border-secondary'
					: ''}"
				on:click={() => onClickCurrentTeamSwitch(idx)}
			>
				{team.name}
			</button>
		</div>
	{/each}
</div>
