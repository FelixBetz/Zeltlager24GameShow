import { API_URL } from './apiUrl';

export enum ListGameState {
	IDLE = 'IDLE',
	WAIT_DRAW = 'WAIT_DRAW',
	PLAY = 'PLAY'
}

export interface ListGameItem {
	label: string;
	value: number;
	index: number;
	isPlaced: boolean;
	isStartItem: boolean;
	isShowValue: boolean;
}

export interface ListGameData {
	itemsSorted: ListGameItem[];
	placedItems: ListGameItem[];
	itemsRandom: ListGameItem[];
	minValue: string;
	maxValue: string;
	question: string;
	state: ListGameState;
}

export function getDefaultListGameDate(): ListGameData {
	return {
		itemsSorted: [],
		placedItems: [],
		itemsRandom: [],
		minValue: '',
		maxValue: '',
		question: '',
		state: ListGameState.IDLE
	};
}

export function apiListGameGetData(): Promise<ListGameData> {
	const response = fetch(API_URL + 'list_game/data')
		.then((response) => response.json())
		.then((response: ListGameData) => response)
		.catch(() => getDefaultListGameDate());

	return response;
}

export function apiListGamePlaceItem(pIndex: number, pPositon: number): Promise<boolean> {
	const formData = new FormData();
	formData.append('index', pIndex.toString());
	formData.append('position', pPositon.toString());

	const response = fetch(API_URL + 'list_game/place', {
		method: 'POST',
		body: formData
	})
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiListGameSwitchState(pState: string): Promise<boolean> {
	const response = fetch(API_URL + 'list_game/switchState?state=' + pState)
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}
export function apiListGameSwitchCurrentTeam(pTeam: number): Promise<boolean> {
	const response = fetch(API_URL + 'admin/switchCurrentTurn?team=' + pTeam)
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiListGameShowValues(pIsShowValues: boolean): Promise<boolean> {
	const response = fetch(API_URL + 'list_game/showValues?showValues=' + (pIsShowValues ? '1' : '0'))
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}
