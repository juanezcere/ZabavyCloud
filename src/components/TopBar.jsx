import { useContext } from 'react';
import { Navbar, NavbarBrand, NavbarContent, NavbarMenuToggle, Tooltip } from '@nextui-org/react';
import { AppContext } from '../AppContext';

import { AcmeLogo } from './Images';

import { MainMenu } from './topbar/MainMenu';
import { LanguageChanger } from './topbar/LanguageChanger';
import { ThemeChanger } from './topbar/ThemeChanger';

export const TopBar = () => {
    const { isMenuOpen, setIsMenuOpen } = useContext(AppContext);
    return (
        <Navbar maxWidth='xl' onMenuOpenChange={setIsMenuOpen}>
            <NavbarContent justify='start'>
                <Tooltip content={isMenuOpen ? 'Close menu' : 'Open menu'}>
                    <NavbarMenuToggle aria-label={isMenuOpen ? 'Close menu' : 'Open menu'} />
                </Tooltip>
                <MainMenu />
            </NavbarContent>
            <NavbarContent justify='center'>
                <Tooltip content='Juanez'>
                    <NavbarBrand>
                        <AcmeLogo />
                        <h1 className='font-bold text-inherit'>Juanez ™</h1>
                    </NavbarBrand>
                </Tooltip>
            </NavbarContent>
            <NavbarContent justify='end'>
                <ThemeChanger />
                <LanguageChanger />
            </NavbarContent>
        </Navbar>
    );
};
