# Stlyle Clashing

Style clashing is a Problem which occures, when multiple components use the same namspace for there Components. 

the solution is t install a external Libary named styled-components 

## Installation

```
yarn add styled-components
```

## HOW to use styled-components

### Inside the Style Component
- Switch the Scss files into jsx files
- import the Libary into the scss File 
    ```
    import styled from 'styled-component'
    ```
- create a Variable which contains the Scss code

Example:

```
import styled from 'styled-components'

export const NavigationContainer = styled.div'
    height: 70px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 25px;
'

```



### Inside the jsx Component 

- import the style component
```
import {NavigationContainer} from './navigation.styles'
```
- replace all classes with the Components


Example:


```
return (
      <Fragment>
        <NavigationContainer>
            <LogoContainer to='/'>
                <CrwnLogo className='logo'/>
            </LogoContainer>
            
            <NavigationLinks>
                <NavLink to= '/shop'>
                    SHOP
                </NavLink>
                {currentUser ? (
            <NavLink as='span' onClick={signOutUser}>
              SIGN OUT
            </NavLink>
            ) : (
            <NavLink to='/auth'>
              SIGN IN
            </NavLink>
          )}
           <CartIcon/>     
        </NavigationLinks>
        {isCartOpen && <CartDropdown/>}
        </NavigationContainer>
        <Outlet />
      </Fragment>
    )
```

!notice at NavLink Iam able to use as to specifie as which element it should render 


### Style over existing styles

- import Link into the styles Component
  ```
  import {Link} from 'react-router-dom'
  ```

- implement into the actual code 

  ```
  export const LogoContainer = styled(Link)'
    height: 100%;
    width: 70px;
    padding: 25px;'
  ```

### Extend Styling 
- create a base styling 
```
export const BaseButton = styled.button'
  min-width: 165px;
  '
```
- extend the base styling 
```
export const GoogleSignInButton = styled(BaseButton'
background-color: #4285f4;
color: white;
'
```


### Overwrite Component Styling

To target the Styling of a external Component which is a child of the styling component. 

- import the Child from the external component
```
import {BaseButton, 
GoogleSignInButton, 
InvertedButton}
from './button.styles.jsx'

```
- nest and style the component child 

```
export const CartDropdownContainer = styled.div'
  position: absolute;
  width: 240px;
  height: 340px;
  ${BaseButton},
  ${GoogleSignInButton},
  ${InvertedButton}{
    margin-top: auto;
  }'
```

### Style SVG's inside Style components

You also are able to style components inside the Style Component.

- import the SVG into the style componend
```
import { ReactComponent as ShoppingIcon } from '../../assets/shopping-bag.svg';
```

- Use the SVG as a attribute inside the styled function call 

```
export const ShoppingIcon = styled(ShoppingSvg)'
  width: 24px;
  height: 24px;
'
```

### Send values from the Component to the styled component

To send values like urls, diffrent colors... to the styled component it is nessecary to declare the value inside the Component. 

- Component.jsx:
```
<div className="background-image" imageUrl= {imageUrl} />
```

- Styled component:

```
background-image: ${({imageUrl})=>`url(${imageUrl})`}
```

a functioncallback inside the styled component is declared where the value from component.jsx is destructured and returned as a value for the Styling
