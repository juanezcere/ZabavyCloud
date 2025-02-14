import { Navbar, NavbarBrand, NavbarContent, Tooltip, AvatarGroup, Avatar } from '@nextui-org/react';

import { AcmeLogo } from './Images';

export const FootBar = () => {
    const buildWith = [
        { name: 'vite', title: 'ViteJS', icon: '/vite.png', href: 'https://vitejs.dev/' },
        { name: 'react', title: 'ReactJS', icon: '/react.png', href: 'https://react.dev/' },
        { name: 'tailwind', title: 'TailwindCSS', icon: '/tailwind.png', href: 'https://tailwindcss.com/' },
        { name: 'nextui', title: 'NextUI', icon: '/nextui.png', href: 'https://nextui.org/' },
    ]
    return (
        <Navbar maxWidth='xl' position='bottom'>
            <NavbarContent justify='start'>
                <h3 className='text-foreground'>Build with:</h3>
                <AvatarGroup isBordered>
                    {buildWith.map((item, i) => {
                        return (
                            <Tooltip
                                key={`${item.name}_${i}`}
                                content={item.title}
                            >
                                <Avatar src={item.icon} className='p-1' />
                            </Tooltip>
                        )
                    })}
                </AvatarGroup>
            </NavbarContent>
            <NavbarContent justify='center'>
                <Tooltip content='Juanez'>
                    <NavbarBrand>
                        <AcmeLogo />
                    </NavbarBrand>
                </Tooltip>
            </NavbarContent>
            <NavbarContent className='hidden md:flex' justify='end'>
                <h5 className='text-inherit'>{new Date().getFullYear()}</h5>
            </NavbarContent>
        </Navbar>
    );
};
