import camelcase from "lodash.camelcase";

// Преобразует пришедшие данные для работы на фронтенде
const transformResult = (result) => {
  const transformedResult = {};
  for (const entry of Object.entries(result)) {
    // Переводим ключи в camelCase
    const key = camelcase(entry[0]);
    transformedResult[key] = entry[1];
  }

  return transformedResult;
};

// Делает запрос JSON данных
const doFetchForJson = async (url) => {
  const response = await fetch(url);
  // TODO Решить как обрабатывать ошибки
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  const jsonData = await response.json();
  return jsonData;
};

// Делает запрос одной записи из API
const doFetchSingleItem = async (url) => {
  const item = await doFetchForJson(url);
  return transformResult(item);
};

// Делает полный запрос списка записей из API
const doFetchFullResults = async (url) => {
  const results = await doFetchForJson(url);
  return results.map((result) => transformResult(result));
};

// Делает POST запрос
const doPostFetch = async (url, data) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: data,
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response;
};

// Делает DELETE запрос
const doDeleteFetch = async (url, data) => {
  const response = await fetch(url, { method: "DELETE", body: data });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response;
};

export {
  transformResult,
  doFetchForJson,
  doFetchSingleItem,
  doFetchFullResults,
  doPostFetch,
  doDeleteFetch,
};
