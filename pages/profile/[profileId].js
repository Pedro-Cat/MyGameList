import React from 'react'

import { useRouter } from 'next/router'

function ProfilePage(){
    const router = useRouter();

    const profileId = router.query.profileId; //Necesário para pegar a id
    //Send a request to the backend API
    //To fetch the Profile item wiht profileId

    return <h1>Profile Page</h1>
}

export default ProfilePage;