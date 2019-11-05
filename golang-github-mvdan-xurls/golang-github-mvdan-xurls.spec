%global globalversion   2.0.0

%global goipath         github.com/mvdan/xurls
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Extract urls from text using regular expressions.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Extract urls from text using regular expressions.

License:                Custom
URL:                    %{gourl}
Source0:                %{gosource}

Provides:               golang(mvdan.cc/xurls/v2) = %{version}-%{release}


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
