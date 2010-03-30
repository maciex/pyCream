
// STL
typedef std::pair<long, long> stdPairLongLong;
typedef std::pair<std::string, long>  stdPairStringLong;
typedef std::pair<std::string, std::string>  stdPairStringString;
typedef std::allocator<char> stdAllocatorChar;


// Cream typedef classes
typedef std::list<JobDescriptionWrapper*> RegisterArrayRequest;


typedef boost::tuple<std::string, std::string, std::string> StringStringString;
typedef boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> RegisterResult;
typedef std::map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string> > RegisterArrayResult;


typedef std::map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string> > StatusArrayResult;
typedef std::map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string> > InfoArrayResult;

