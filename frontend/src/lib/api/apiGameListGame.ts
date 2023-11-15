import { API_URL } from './apiUrl';

export interface ListGameItem {
	label: string;
	value: number;
	index: number;
	isPlaced: boolean;
	isStartItem: boolean;
}

export interface ListGameData {
	itemsSorted: ListGameItem[];
	placedItems: ListGameItem[];
	itemsRandom: ListGameItem[];
	minValue: string;
	maxValue: string;
	question: string;
}

export function getDefaultListGameDate(): ListGameData {
	return {
		itemsSorted: [],
		placedItems: [],
		itemsRandom: [],
		minValue: '',
		maxValue: '',
		question: ''
	};
}

export function apiGetListGameData(): Promise<ListGameData> {
	const response = fetch(API_URL + 'list_game/data')
		.then((response) => response.json())
		.then((response: ListGameData) => response)
		.catch(() => getDefaultListGameDate());

	return response;
}

export function apiPlaceItem(pIndex: number, pPositon: number): Promise<boolean> {
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
