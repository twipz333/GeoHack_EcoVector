import { createAsyncThunk } from "@reduxjs/toolkit";
import { API_URLS } from "../../app/api/apiConfig";
import {
  doFetchSingleItem,
  doFetchFullResults,
  doPostFetch,
  doDeleteFetch,
} from "../../app/api/apiHelpers";

const createUser = createAsyncThunk(
  "user/createUser",
  async (userData, { rejectWithValue }) => {
    const url = `${API_URLS.base}${API_URLS.users}`;
    try {
      const response = await doPostFetch(url, userData);
      const result = await response.json();
      console.log(result);
      return result;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const deleteUser = createAsyncThunk(
  "user/deleteUser",
  async (userId, { rejectWithValue }) => {
    const url = `${API_URLS.base}${API_URLS.users}`;
    try {
      const response = await doDeleteFetch(url, { userId });
      console.log(response);
      return response;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const fetchUsersList = createAsyncThunk(
  "user/fetchUsersList",
  async (_, { rejectWithValue }) => {
    const url = `${API_URLS.base}${API_URLS.users}`;
    try {
      const results = await doFetchFullResults(url);
      return { result: results };
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const fetchUser = createAsyncThunk(
  "user/fetchUser",
  async (userId, { rejectWithValue }) => {
    const url = `${API_URLS.base}${API_URLS.users}${userId}`;
    try {
      const result = await doFetchSingleItem(url);
      return result;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const loginUser = (userId) => {
  return (dispatch) => {
    dispatch(fetchUser(userId));
    localStorage.set("userId", userId);
  };
};

export { createUser, deleteUser, fetchUsersList, fetchUser, loginUser };
