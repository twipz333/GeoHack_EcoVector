import React, { useEffect } from "react";
// import { useDispatch, useSelector } from 'react-redux';
// import { useParams } from 'react-router';
// import { selectCatalogStatus } from '../catalogSelectors';
// import { fetchCatalogCategory } from '../catalogFetchThunks';
// import { LoadingMessage } from '../messages/LoadingMessage';
// import { ErrorMessage } from '../messages/ErrorMessage';
import { ActivitiesList } from "./ActivitiesList";
import { activitiesData } from "./activitiesData";

export const Activities = () => {
  // Получаем тип элемента из адресной строки
  // const { type } = useParams();

  // Данные о статусе запроса
  // const [fetchStatus, fetchError] = useSelector(selectCatalogStatus);

  // const dispatch = useDispatch();

  // useEffect(() => {
  //   dispatch(fetchCatalogCategory(type));
  // }, [type, dispatch]);

  return (
    <>
      {/* {fetchStatus === "loading" && <LoadingMessage />}
        {fetchError && <ErrorMessage error={fetchError} />} */}
      <ActivitiesList activities={activitiesData} />
    </>
  );
};
