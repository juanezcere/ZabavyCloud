import { useContext, useState, useMemo } from 'react';
import { Avatar, Dropdown, DropdownTrigger, Button, DropdownMenu, DropdownItem, Tooltip } from '@nextui-org/react';
import { AppContext } from '../../AppContext';

export const LanguageChanger = () => {
    const { isMobile, languages, language, setLanguage } = useContext(AppContext);
    const [icon, setIcon] = useState('');
    useMemo(() => {
        console.log('Changing language icon:', language);
        const lang = languages.filter((l) => language === l.id);
        if (lang.length) setIcon(lang[0].icon);
    }, [language]);
    return (
        <Dropdown backdrop={isMobile ? 'transparent' : 'blur'}>
            <DropdownTrigger>
                <Button
                    color='primary'
                    variant='light'
                    shortcut='⌘N'
                    startContent={
                        <Avatar
                            showFallback
                            src={icon}
                            name={language}
                            size='sm'
                        />
                    }
                >
                </Button>
            </DropdownTrigger>
            <DropdownMenu
                variant='faded'
                aria-label='Select the lenguage'
                selectionMode='single'
                className='text-foreground bg-background'
                selectedKeys={language}
                onAction={setLanguage}
            >
                {languages.map((lang) => {
                    return (
                        <DropdownItem
                            key={lang.id}
                            description={lang.description}
                            startContent={
                                <img src={lang.icon} />
                            }
                        >
                            {lang.title}
                        </DropdownItem>
                    );
                })}
            </DropdownMenu>
        </Dropdown>
    );
};
