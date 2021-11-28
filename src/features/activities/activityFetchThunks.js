import { createAsyncThunk } from "@reduxjs/toolkit";
import { API_URLS } from "../../auxiliary/API/apiConfig";
import {
  doFetchSingleItem,
  doFetchFullResults,
} from "../../auxiliary/API/apiHelpers";
import { selectCatalogItem } from "./activitySelectors";

// Запускает запрос элемента, если его нет в кеше
const getCatalogItemThunk = ({ type, id, url }) => {
  return (dispatch, getState) => {
    const item = selectCatalogItem(getState(), type, { id, url });
    if (!item) {
      dispatch(fetchCatalogItem({ type, id, url }));
    }
  };
};

// Thunk для запроса каталога по категории
const fetchCatalogCategory = createAsyncThunk(
  "catalog/fetchCatalogCategory",
  async (type, { rejectWithValue }) => {
    const fullUrl = `${API_URLS.base}${API_URLS[type]}`;
    try {
      const results = await doFetchFullResults(fullUrl);
      return { type, result: results };
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Thunk для запроса одного элемента каталога
const fetchCatalogItem = createAsyncThunk(
  "catalog/fetchCatalogItem",
  async ({ type, id, url }, { rejectWithValue }) => {
    // TODO Добавить форматирование url
    const fullUrl = url || `${API_URLS.base}/${type}/${id}`;
    if (!fullUrl) {
      rejectWithValue("Некорректные входные данные");
    }
    try {
      const result = await doFetchSingleItem(fullUrl);
      type = type || result.type;
      return { type, result };
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export { getCatalogItemThunk, fetchCatalogCategory, fetchCatalogItem };
