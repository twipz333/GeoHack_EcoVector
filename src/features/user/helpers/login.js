export const getCurrUserId = () => {
  const userId = localStorage.get("userId");
  return userId || null;
};
