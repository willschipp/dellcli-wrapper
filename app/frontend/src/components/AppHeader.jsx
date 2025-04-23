import React from 'react';

import { Content, Header, Heading } from '@adobe/react-spectrum';

import WebPage from '@spectrum-icons/workflow/WebPage';

function AppHeader() {

    return (
        <Content margin="size-200">
            <Header>
                <Heading level={2}>
                    <WebPage/>
                    &nbsp;
                    DellCTL UX
                </Heading>
            </Header>
        </Content>
    )
}

export default AppHeader;