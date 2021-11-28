import React from 'react';

// Список фильмов
export function ErrorMessage({ error }) {
    return (
        <div className="error-message">
            Ошибка: {error || 'Произошла ошибка'}
        </div>
    );
}
