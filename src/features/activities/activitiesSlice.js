import { createSlice } from "@reduxjs/toolkit";
import { fetchActivityItem } from "./activityFetchThunks";
import { setPending, setError, addItemToCache, resetStatus } from "./helpers";

const initialState = {
  cache: [],
  status: "idle",
  error: null,
};

const activitySlice = createSlice({
  name: "activity",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchActivityItem.pending, (state) => {
        setPending(state);
      })
      .addCase(
        fetchActivityItem.fulfilled,
        (state, { payload: { type, result } }) => {
          resetStatus(state);
          addItemToCache(state, type, result);
        }
      )
      .addCase(
        fetchActivityItem.rejected,
        (state, { error: { message }, payload: error }) => {
          setError(state, `${message}: ${error}`);
        }
      );
  },
});

// Получаем и экспортируем reducer и action creator
const activityReducer = activitySlice.reducer;

export { activityReducer };
