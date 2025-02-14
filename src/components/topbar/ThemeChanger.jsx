import { useContext } from 'react';
import { Switch, Tooltip } from '@nextui-org/react';
import { AppContext } from '../../AppContext';

import { MoonIcon, SunIcon } from '../Images';

export const ThemeChanger = () => {
    const { contrastMode, setContrastMode } = useContext(AppContext);
    return (
        <Switch
            defaultSelected={contrastMode}
            onValueChange={setContrastMode}
            size='sm'
            color='warning'
            thumbIcon={({ isSelected, className }) =>
                isSelected ? (
                    <SunIcon className={className} />
                ) : (
                    <MoonIcon className={className} />
                )
            }
        />
    );
};
