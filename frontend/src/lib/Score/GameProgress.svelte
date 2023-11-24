<script lang="ts">
	import { API_URL } from '$lib/api/apiUrl';
	import type { Game } from '$lib/types';
	import Crown from '../Icons/Crown.svelte';

	export let game: Game;
	export let colors: string[];

	interface GameScore {
		isGamePlayed: boolean;
		winnerAvatar: string;
		gameName: string;
		color: string;
	}

	let avatarWinners = [
		'avatars/bird.png',
		'avatars/owl.png',
		'avatars/lion.png',
		'avatars/bird.png',
		'avatars/bird.png'
	];

	let gameScores: GameScore[] = [];
	$: gameScores = createGameScore(game);
	function createGameScore(pGame: Game): GameScore[] {
		let retScores: GameScore[] = [];

		for (let i = 0; i < pGame.gamesToPlay; i++) {
			let isPlayed = i < pGame.gamesPlayed;

			retScores[retScores.length] = {
				isGamePlayed: isPlayed,
				winnerAvatar: avatarWinners[i],
				gameName: 'Spiel ' + (i + 1),
				color: isPlayed ? colors[i % colors.length] : 'var(--bs-gray-600)'
			};
		}

		return retScores;
	}
</script>

<div class="card mb-3">
	<div class="card-body pb-0">
		<div class="steps d-flex flex-wrap flex-sm-nowrap justify-content-between">
			{#each gameScores as score}
				<div class="step" class:completed={score.isGamePlayed}>
					<div class="step-icon-wrap" style="--score-color:{score.color}">
						<div class="step-icon" style="background-color: {score.color};  ">
							<div class="position-relative crown">
								<div class="position-absolute top-0 start-50 translate-middle">
									<Crown color={score.color} />
								</div>
								{#if score.isGamePlayed}
									<img src={API_URL + 'assets/' + score.winnerAvatar} alt="Winner" />
								{/if}
							</div>
						</div>
					</div>
					<h4 class="step-title" style="color: {score.color}">{score.gameName}</h4>
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.steps {
		padding-top: 25px;
	}
	.steps .step {
		display: block;
		width: 100%;
		margin-bottom: 35px;
		text-align: center;
	}

	.steps .step .step-icon-wrap {
		display: block;
		position: relative;
		width: 100%;
		height: 80px;
		text-align: center;
	}

	.steps .step .step-icon-wrap::before,
	.steps .step .step-icon-wrap::after {
		display: block;
		position: absolute;
		top: 50%;
		width: 50%;
		height: 10px;
		margin-top: -1px;
		background-color: var(--score-color);
		content: '';
		z-index: 1;
	}

	.steps .step .step-icon-wrap::before {
		left: 0;
	}

	.steps .step .step-icon-wrap::after {
		right: 0;
	}

	.steps .step .step-icon {
		display: inline-block;
		position: relative;
		width: 80px;
		height: 80px;
		border-radius: 50%;

		font-size: 38px;
		line-height: 81px;
		z-index: 5;
	}

	.steps .step .step-title {
		margin-top: 16px;
		margin-bottom: 0;
	}

	.step-title {
		font-size: 2rem;
		font-weight: 600;
	}

	.steps .step:first-child .step-icon-wrap::before {
		display: none;
	}

	.steps .step:last-child .step-icon-wrap::after {
		display: none;
	}

	.steps .step.completed .step-icon-wrap::before,
	.steps .step.completed .step-icon-wrap::after {
		background-color: var(--score-color);
	}

	img {
		padding: 10px;
		margin-top: 12px;
		width: 100%;
		height: 100%;
	}

	.crown {
		margin-top: -10px;
	}
</style>
