import styled from 'styled-components'

export const Container = styled.div`
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  background: linear-gradient(to bottom, #f2f2f2 0%, #333 100%);
  overflow: hidden;
`
export const ReaderContainer = styled.div`
  font-size: 16px;
  position: absolute;
  top: 0px;
  left: 0rem;
  right: 0rem;
  bottom: 0rem;
  transition: all 0.6s ease;
`
const Button = styled.button`
  font-family: inherit;
  font-size: inherit;
  border: none;
  outline: none;
  cursor: pointer;
  user-select: none;
  appearance: none;
  background: none;
`
