
// STL
typedef std::pair< long, long > stdPairLongLong;
typedef std::pair< std::string, long > stdPairStringLong;
typedef std::pair< std::string, std::string > stdPairStringString;

typedef std::map< std::string, std::string > stdMapStringString;

typedef std::vector< std::string > stdVectorString;
typedef std::allocator< char > stdAllocatorChar;


// Cream typedef classes
typedef boost::tuple< JobIdWrapper::RESULT, JobIdWrapper, std::string > TupleJobIdWrapper;
typedef boost::tuple< JobStatusWrapper::RESULT, JobStatusWrapper, std::string > TupleJobStatusWrapper;
typedef boost::tuple< JobInfoWrapper::RESULT, JobInfoWrapper, std::string > TupleJobInfoWrapper;

typedef std::map< std::string, boost::tuple<JobIdWrapper::RESULT, JobIdWrapper, std::string > > RegisterArrayResult;
typedef std::map< std::string, boost::tuple<JobStatusWrapper::RESULT, JobStatusWrapper, std::string > > StatusArrayResult;
typedef std::map< std::string, boost::tuple<JobInfoWrapper::RESULT, JobInfoWrapper, std::string > > InfoArrayResult;

typedef std::vector< JobIdWrapper > stdVectorJobIdWrapper;
typedef std::vector< JobPropertyWrapper > stdVectorJobPropertyWrapper;
typedef std::vector< JobStatusWrapper > stdVectorJobStatusWrapper;

typedef std::list< JobDescriptionWrapper* > RegisterArrayRequest;

