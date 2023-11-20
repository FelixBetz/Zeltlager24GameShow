<script lang="ts">
	import ListGameAdmin from '../../lib/Games/ListGame/ListGameAdmin.svelte';
	import AvatarImage from '$lib/AvatarImage.svelte';
	import CreateTeamsAdmin from '$lib/CreateTeams/CreateTeamsAdmin.svelte';

	import { apiAdminSwitchState, apiDeleteTeam } from '$lib/api/apiAdmin';
	import { apiGetGame } from '$lib/api/apiGame';
	import { GameState, type Game, getDefaultGame } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
	import { apiListGameSwitchCurrentTeam } from '$lib/api/apiGameListGame';

	const states: string[] = Object.values(GameState);

	function onClickSwitchState(pState: string) {
		if (Object.values(GameState).includes(pState as GameState)) {
			game.state = GameState[pState as keyof typeof GameState];
		}
		apiAdminSwitchState(pState);
	}

	let intervalGameState: string | number | NodeJS.Timeout | undefined;
	let game: Game = getDefaultGame();
	let isRequestOngoing = false;
	async function cyclicInterval() {
		if (!isRequestOngoing) {
			isRequestOngoing = true;
			game = await apiGetGame();
			isRequestOngoing = false;
		}
	}

	onMount(() => {
		intervalGameState = setInterval(cyclicInterval, 1000);
	});

	onDestroy(() => {
		clearInterval(intervalGameState);
	});

	function onClickCurrentTeamSwitch(pNum: number) {
		game.currentTurnTeam = pNum;

		apiListGameSwitchCurrentTeam(pNum);
	}

	function deleteTeam(pIdx: number) {
		game.teams.splice(pIdx, 1);
		game = game;
		apiDeleteTeam(pIdx);
	}
</script>

<div class="row">
	<div class="col-2">
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
	</div>
	<div class="col-3">
		<h1>Teams</h1>
		<div class="row">
			<div class="col-12">
				{#each game.teams as team, idx}
					<div class="card">
						<div class="d-flex">
							<div><AvatarImage avatar={team.avatar_url} /></div>
							<div><button class="transparent-button"><i class="bi bi-plus-circle" /></button></div>
							<div>{team.total_score}</div>
							<div><button class="transparent-button"><i class="bi bi-dash-circle" /></button></div>
							<div>
								<button class="transparent-button" on:click={() => deleteTeam(idx)}
									><i class="bi bi-trash" /></button
								>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
		<hr />
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
	</div>
	<div class="col-7">
		<h1>Game</h1>

		{#if game.state == GameState.IDLE}
			IDLE
		{:else if game.state === GameState.CREATING_TEAMS}
			<CreateTeamsAdmin />
		{:else if game.state === GameState.GAME_1}
			<ListGameAdmin />
		{:else if game.state == GameState.GAME_2}
			IDLE
		{:else if game.state == GameState.GAME_3}
			IDLE
		{:else if game.state == GameState.GAME_4}
			IDLE
		{:else if game.state == GameState.GAME_5}
			IDLE
		{:else if game.state == GameState.SCORE}
			IDLE
		{/if}
	</div>
</div>

<style>
	.transparent-button {
		background-color: transparent;
		border: 0px;
	}
</style>
