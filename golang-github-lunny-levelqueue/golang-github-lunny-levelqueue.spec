%global goipath         github.com/lunny/levelqueue
%global commit          02b525a4418e684a7786215296984e364746806f
%global scm             git

%gometa

%global common_description %{expand:
Level queue is a simple queue golang library base on go-leveldb.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Level queue is a simple queue golang library base on go-leveldb.

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
