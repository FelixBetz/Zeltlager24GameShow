export enum GameState {
	IDLE = 'IDLE',
	CREATING_TEAMS = 'CREATING_TEAMS',
	GAME_1 = 'GAME_1',
	GAME_2 = 'GAME_2',
	GAME_3 = 'GAME_3',
	GAME_4 = 'GAME_4',
	GAME_5 = 'GAME_5',
	SCORE = 'SCORE'
}

export interface Team {
	avatar_url: string;
	name: string;
	shortcut: string;
	scores: number[];
	total_score: number;
	game_life: number;
}

export interface CurrentTeam {
	team: Team;
	isShow: boolean;
}

export interface Game {
	teams: Team[];
	state: GameState;
	currentTurnTeam: number;
}

export function getDefaultGame(): Game {
	return { teams: [], state: GameState.IDLE, currentTurnTeam: -1 };
}
