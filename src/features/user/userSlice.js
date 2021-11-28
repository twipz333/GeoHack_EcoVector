import { createSlice } from "@reduxjs/toolkit";
import {
  createUser,
  deleteUser,
  fetchUsersList,
  fetchUser,
} from "./userThunks";
import { setPending, setError, resetStatus } from "./helpers";

const initialState = { data: null, status: "idle", error: null };

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    logOutUser(state) {
      state.data = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(createUser.pending, (state) => {
        setPending(state);
      })
      .addCase(createUser.fulfilled, (state, { payload: result }) => {
        resetStatus(state);
        state.data = result;
      })
      .addCase(
        createUser.rejected,
        (state, { error: { message }, payload: error }) => {
          setError(state, `${message}: ${error}`);
        }
      )
      .addCase(fetchUser.pending, (state) => {
        setPending(state);
      })
      .addCase(fetchUser.fulfilled, (state, { payload: { result } }) => {
        resetStatus(state);
        state.data = result;
      })
      .addCase(
        fetchUser.rejected,
        (state, { error: { message }, payload: error }) => {
          setError(state, `${message}: ${error}`);
        }
      )
      .addCase(deleteUser.pending, (state) => {
        setPending(state);
      })
      .addCase(deleteUser.fulfilled, (state) => {
        resetStatus(state);
      })
      .addCase(
        deleteUser.rejected,
        (state, { error: { message }, payload: error }) => {
          setError(state, `${message}: ${error}`);
        }
      );
  },
});

export function selectUser(state) {
  return state.user;
}

export const { logInUser, logOutUser } = userSlice.actions;
export const userReducer = userSlice.reducer;
