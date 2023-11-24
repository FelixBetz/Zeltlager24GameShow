<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiDeleteTeam } from '$lib/api/apiAdmin';
	import type { Game } from '$lib/types';

	export let game: Game;

	function deleteTeam(pIdx: number) {
		game.teams.splice(pIdx, 1);
		game = game;
		apiDeleteTeam(pIdx);
	}
</script>

<h1>Teams</h1>
<div class="row">
	<div class="col-12">
		{#each game.teams as team, idx}
			<div class="card">
				<div class="d-flex">
					<div><AvatarImage avatar={team.avatar_url} /></div>
					<div class="ps-3" style="font-size: 1.5rem">
						Team {team.name} ({team.total_score} Punkte)
					</div>

					<!--<div><button class="transparent-button"><i class="bi bi-plus-circle" /></button></div>
							<div>{team.total_score}</div>
							<div><button class="transparent-button"><i class="bi bi-dash-circle" /></button></div>
							<div>
								<button class="transparent-button" on:click={() => deleteTeam(idx)}>
									<i class="bi bi-trash" />
								</button>
							</div>-->
				</div>
			</div>
		{/each}
	</div>
</div>
