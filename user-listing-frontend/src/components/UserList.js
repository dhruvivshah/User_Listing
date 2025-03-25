//react view for the user list 
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import UserDetail from './UserDetail'; 
import './User List.css'; 

const UserList = () => {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5; // Number of items to display per page
    const [selectedUser , setSelectedUser ] = useState(null); // State to hold selected user

    useEffect(() => {
        const fetchUsers = async () => {
            const response = await axios.get('http://localhost:8000/api/users/'); //read data from the api and show in paginated manner
            setUsers(response.data.results);
            setLoading(false);
        };
        fetchUsers();
    }, []);

    // Calculate current items and display according to the page size
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = users.slice(indexOfFirstItem, indexOfLastItem);

    // Change page to show the other output
    const handlePageChange = (pageNumber) => {
        setCurrentPage(pageNumber);
        setSelectedUser (null); // Clear selected user when changing pages
    };

    const handleUserClick = (user) => {
        setSelectedUser (user); // Set the selected user and display user details
    };

    const handleBack = () => {
        setSelectedUser (null); // Clear the selected user and show the user list
    };

    if (loading) return <div>Loading...</div>;

    return (
        <div className="user-list">
            {selectedUser  ? (
                <UserDetail user={selectedUser } onBack={handleBack} /> // Show user detail
            ) : (
                <>
                    <h1>User List</h1>
                    <ul>
                        {currentItems.map(user => (
                            <li key={user.id} onClick={() => handleUserClick(user)}>
                                {user.name} - {user.email}
                            </li>
                        ))}
                    </ul>
                    <div className="pagination">
                        {Array.from({ length: Math.ceil(users.length / itemsPerPage) }, (_, index) => (
                            <button key={index + 1} onClick={() => handlePageChange(index + 1)}>
                                {index + 1}
                            </button>
                        ))}
                    </div>
                </>
            )}
        </div>
    );
};

export default UserList;

