import Header from "./Header/header";

const Layout = ({children}) => {
    return (
        <div>
            <Header className="bodyHeader"/>
            {children}
        </div>
    );
}
 
export default Layout;