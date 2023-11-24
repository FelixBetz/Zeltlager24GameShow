<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiDeleteTeam, apiIncrementTeamLife, apiDecrementTeamLife } from '$lib/api/apiAdmin';
	import type { Game } from '$lib/types';

	export let game: Game;

	let lifes = [0, 1, 2, 3, 4];

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
			<div
				class="d-flex mt-2 rounded flex-wrap {game.currentTurnTeam == idx
					? 'border border-5 border-secondary'
					: ''}"
				style="background-color: var(--bs-body-bg);"
			>
				<div class="">
					<AvatarImage avatar={team.avatar_url} size={100} />
				</div>
				<div class="flex-grow-1">
					<div class="d-flex flex-column flex-wrap text-center">
						<div class="w-100" style="font-size: 1.5rem">
							Team {team.name} ({team.total_score} Punkte)
						</div>

						<div class="d-flex fs-3 text-center justify-content-center">
							<button
								class="transparent-button btn p-1 me-2"
								on:click={() => apiDecrementTeamLife(idx)}
							>
								<i class="bi bi-dash-circle" />
							</button>
							{#each lifes as life}
								<i
									class="bi bi-heart-fill p-1"
									style="color: {life < team.game_life ? 'red' : 'var(--bs-dark)'};"
								/>
							{/each}
							<button
								class="transparent-button btn p-1 ms-2"
								on:click={() => apiIncrementTeamLife(idx)}
							>
								<i class="bi bi-plus-circle" />
							</button>
						</div>
					</div>
				</div>
			</div>
		{/each}
	</div>
</div>

<!--<div><button class="transparent-button"><i class="bi bi-plus-circle" /></button></div>
							<div><button class="transparent-button"><i class="bi bi-dash-circle" /></button></div>
							<div>
								<button class="transparent-button" on:click={() => deleteTeam(idx)}>
									<i class="bi bi-trash" />
								</button>
							</div>-->
<style>
	.transparent-button {
		margin: 0px;

		font-size: 1.75rem;
		background-color: transparent;
		border: 9px;
	}
</style>
