import React from 'react'

const CenteredMessage = ({text}) => {
  return (
    <div className='centered-message'>
    <span className="badge rounded-pill bg-secondary">
      {text}
    </span>
  </div>
  )
}

export default CenteredMessage
