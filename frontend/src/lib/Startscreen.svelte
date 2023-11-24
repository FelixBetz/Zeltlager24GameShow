<div style="height: 100vh;  display: flex; align-items: center; justify-content: center;">
	<svg width="100%" height="100%">
		<text x="50%" y="40%" text-anchor="middle">
			<tspan x="50%" dy="0em">Themen</tspan>
			<tspan x="50%" dy="1em"> Show </tspan>
		</text>
	</svg>
</div>

<style>
	svg text tspan {
		letter-spacing: 10px;
		stroke: var(--bs-secondary);
		font-size: 14rem;
		font-weight: 900;
		stroke-width: 8;
		animation: textAnimate 7s infinite alternate;
		text-transform: uppercase;
		text-shadow: 1px 1px 10px var(--bs-secondary), 1px 1px 10px var(--bs-light);
	}

	@keyframes textAnimate {
		0% {
			stroke-dasharray: 0 50%;
			stroke-dashoffset: 20%;
			fill: var(--bs-primary);
		}

		100% {
			stroke-dasharray: 50% 0;
			stroke-dashoffstet: -20%;
			fill: var(--bs-dark);
		}
	}
</style>
