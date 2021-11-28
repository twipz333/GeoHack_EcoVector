import { useLocation } from 'react-router';

/**
 * Получает массив значений параметров адресной строки по ключам
 *
 * @param {Array} keys Массив ключей
 *
 * @return {Array} Массив значений
 */
export function useSearchParams(keys) {
    const searchParams = new URLSearchParams(useLocation().search);
    return keys.map((key) => searchParams.get(key));
}
