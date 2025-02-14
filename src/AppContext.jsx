import { createContext, useState, useEffect } from 'react';
import { languages } from './repository';


export const AppContext = createContext();

export function AppContextProvider(props) {
    //const [repository, setRepository] = useState(new DataModel());
    const [contrastMode, setContrastMode] = useState(() => {
        console.log('Reading contrast from local storage');
        const contrastFromStorage = window.localStorage.getItem('contrast');
        return contrastFromStorage ? (contrastFromStorage === '1') : false;
    });
    const [language, setLanguage] = useState(() => {
        console.log('Reading language from local storage');
        const languageFromStorage = window.localStorage.getItem('language');
        return languageFromStorage ? languageFromStorage : 'english';
    });
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    useEffect(() => {
        console.log('Changing to', (contrastMode ? 'light' : 'dark'), 'mode');
        if (contrastMode) document.documentElement.classList.remove('dark');
        else document.documentElement.classList.add('dark');
        window.localStorage.setItem('contrast', contrastMode ? 1 : 0);
    }, [contrastMode]);
    useEffect(() => {
        console.log('Changing the language to', language);
        window.localStorage.setItem('language', language);
        //fetch(`/${language}.json`).then(r => r.json()).then(r => setRepository(new DataModel(...Object.values(r))));
    }, [language]);
    return (
        <AppContext.Provider
            value={{
                isMobile,
                contrastMode,
                setContrastMode,
                isMenuOpen,
                setIsMenuOpen,
                language,
                setLanguage,
                languages,
            }}
        >
            {props.children}
        </AppContext.Provider>
    );
};
