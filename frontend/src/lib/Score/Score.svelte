<script lang="ts">
	import GameProgress from '$lib/Score/GameProgress.svelte';
	import AvatarImage from '$lib/AvatarImage.svelte';

	import type { Game, Team } from '$lib/types';

	//https://www.learnui.design/tools/data-color-picker.html#single
	const COLORS = ['#f3b84d', '#e49339', '#d36e2c', '#be4825', '#a61a21'];

	const HEIGHT = 30;
	const IMAGE_HEIGHT = 2 * HEIGHT;

	interface BarValue {
		color: string;
		value: number;
	}

	interface ProgressBar {
		values: BarValue[];
	}

	export let game: Game;

	let bars: ProgressBar[] = [];
	$: generateProgressBars(game.teams);
	function generateProgressBars(pTeams: Team[]) {
		let MAX_SCORE = 0;

		pTeams.forEach((team) => {
			let totalScore = team.scores.reduce((acc, currentValue) => acc + currentValue, 0);
			team.total_score = totalScore;
			MAX_SCORE = Math.max(totalScore, MAX_SCORE);
		});

		bars = [];
		pTeams.forEach((team) => {
			let values: BarValue[] = [];
			team.scores.forEach((score, idx) => {
				for (let i = 0; i < score; i++) {
					values.push({ color: COLORS[idx % COLORS.length], value: (1 * 100) / MAX_SCORE });
				}
			});
			bars.push({ values: values });
		});
	}
</script>

<div class="mt-3">
	<GameProgress {game} colors={COLORS} />
</div>
<div class="mt-3">
	{#each bars as bar, barIdx}
		<div
			class=" mt-1 mb-1 p-2 ps-4 rounded-2"
			style="display:flex;  align-items: end; background-color: var(--bs-body-bg);"
		>
			<div class="" style="flex: 1; ">
				<div>
					<div class="title">
						Team {game.teams[barIdx].name}: {game.teams[barIdx].total_score} Punkte
					</div>
				</div>
				<div style="width: 100%; display:flex; ">
					{#each bar.values as value, valueIdx}
						<div
							class="border-3 point"
							style="border-color: {value.color}; width: {value.value}%; background-color: {value.color}; padding:10px; height: {HEIGHT}px; --animation-order:{1 +
								valueIdx}"
							data-animation-offset={1 + valueIdx}
							aria-valuenow={value.value}
							aria-valuemin="0"
							aria-valuemax="100"
						/>
					{/each}
				</div>
			</div>
			<div class="ms-5">
				<AvatarImage avatar={game.teams[barIdx].avatar_url} size={IMAGE_HEIGHT + 20} />
			</div>
		</div>
	{/each}
</div>

<style>
	@keyframes fadeIn {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}
	.point {
		margin-right: 2px;
		font-weight: bolder;
		font-size: 1.3rem;
		opacity: 0;

		animation-name: fadeIn;
		animation-duration: 200ms;
		animation-delay: calc(1000ms +var(--animation-order) * 50ms);
		animation-fill-mode: both;
		animation-timing-function: ease-in-out forwards;
	}

	.point:first-child {
		border-bottom-left-radius: var(--bs-border-radius-xl) !important;
		border-top-left-radius: var(--bs-border-radius-xl) !important;
	}

	.point:last-child {
		border-bottom-right-radius: var(--bs-border-radius-xl) !important;
		border-top-right-radius: var(--bs-border-radius-xl) !important;
	}

	.title {
		font-size: 2rem;
		font-weight: 600;
		color: var(--bs-gray-400);
	}
</style>
