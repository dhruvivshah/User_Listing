import React from 'react';
import './User Detail.css'; //css styling sheet

const UserDetail = ({ user, onBack }) => {
    return (
        <div className="user-detail">
            <h2>User Details</h2>
            <p><strong>Name:</strong> {user.name}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Gender:</strong> {user.gender}</p>
            <p><strong>Phone:</strong> {user.phone}</p>
            <p><strong>Address:</strong> {user.address}</p>
            <button onClick={onBack}>Back to User List</button>
        </div>
    );
};

export default UserDetail;
