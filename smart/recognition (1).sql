-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 11, 2022 at 11:44 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `sid` int(255) NOT NULL,
  `degree` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `date_of_join` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`sid`, `degree`, `fname`, `gender`, `contact_no`, `email_address`, `date_of_join`) VALUES
(1, 'Software', 'george mutembei', 'Male', '9874561230', 'george@gmail.com', '2022-02-23'),
(2, 'bbit', 'John Mwangi', 'Male', '9851645850', 'john@gmail.com', '2022-02-25'),
(3, 'Networking ', 'Goodluck', 'Male', '9704123456', 'good@gmail.com', '2022-03-04'),
(4, 'math', 'james', 'Male', '9874563210', 'james@gmail.com', '2022-03-10');

-- --------------------------------------------------------

--
-- Table structure for table `attendance1`
--

CREATE TABLE `attendance1` (
  `eid` int(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `date_of_join` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance1`
--

INSERT INTO `attendance1` (`eid`, `department`, `fname`, `gender`, `contact_no`, `email_address`, `date_of_join`) VALUES
(1, 'Manager', 'george mutembei', 'Male', '9874561230', 'georgemu@ueab.ac.ke', '2022-03-07');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `attendance1`
--
ALTER TABLE `attendance1`
  ADD PRIMARY KEY (`eid`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `sid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `attendance1`
--
ALTER TABLE `attendance1`
  MODIFY `eid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
