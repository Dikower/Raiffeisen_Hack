import { writable } from "svelte/store";

/**
 * Номер каталога
 */
export const entryCode = writable("");
entryCode.set(localStorage.getItem("entryCode"));

export const summa = writable(0);
export const positions = writable([
  { name: "Кола", code: "189650141", price: 20 },
  { name: "Картошка", code: "102389011", price: 48 },
  { name: "Сыр", code: "189650141", price: 20 },
  { name: "Молоко", code: "102389011", price: 58 },
  { name: "Хлеб", code: "189650141", price: 23 },
  { name: "Булочка", code: "102389011", price: 88 },
  { name: "Масло", code: "189650141", price: 120 },
  { name: "Огурец", code: "102389011", price: 3 },
]);

/**
 * @type {import("svelte/store").Writable<{name:string;code:string;price:number;quantity:number}[]>}
 */
export const finalPositions = writable([]);
